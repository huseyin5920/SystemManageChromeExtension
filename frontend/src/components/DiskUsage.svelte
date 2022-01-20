<script>
    import FusionCharts from "fusioncharts";
    import Widgets from "fusioncharts/fusioncharts.widgets";
    import FusionTheme from "fusioncharts/themes/fusioncharts.theme.fusion";
    import SvelteFC, { fcRoot } from "svelte-fusioncharts";

    import RemoveTrialText from "./tools/removeTrialText.svelte";

    import GetDiskUsage from "../api/DiskUsageComponent/GetDiskUsage";
    import { onMount } from "svelte";

    fcRoot(FusionCharts, Widgets, FusionTheme);

    let total, used, free;

    onMount(async () => {
        const response = await GetDiskUsage();
        total = response.total;
        free = response.free;
        used = response.used;
    });

    $: dataSource = {
        chart: {
            bgColor: "#080e21",
            caption: "Disk Usage",
            showvalues: "1",
            showpercentintooltip: "0",
            numberSuffix: " GB",
            theme: "fusion",
            showValue: "1",
            valueFontColor: "#ffffff",
            valueFontSize: "14",
            baseFontSize: "12",
            baseFontColor: "#ffffff",
            toolTipBgColor: "#000000",
            toolTipBgAlpha: "80",
            toolTipBorderColor: "#666666",
        },
        data: [
            {
                label: "Total Space",
                value: total,
            },
            {
                label: "Available Space",
                value: free,
            },
            {
                label: "Used Space",
                value: used,
            },
        ],
    };

    $: chartConfigs = {
        type: "doughnut3d",
        width: 618,
        height: 300,
        dataFormat: "json",
        dataSource,
    };
</script>

{#key (total, used, free)}
    <div class="m-2 border-2 rounded relative">
        <SvelteFC {...chartConfigs} />
        <RemoveTrialText />
    </div>
{/key}
