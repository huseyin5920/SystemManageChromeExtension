<script>
    import { onMount } from "svelte";

    import GetSystemCpu from "../api/SystemCpuInfoComponent/getSystemCpu";

    import FusionCharts from "fusioncharts";
    import Widgets from "fusioncharts/fusioncharts.widgets";
    import FusionTheme from "fusioncharts/themes/fusioncharts.theme.fusion";
    import SvelteFC, { fcRoot } from "svelte-fusioncharts";

    import RemoveTrialText from "./tools/removeTrialText.svelte";

    fcRoot(FusionCharts, Widgets, FusionTheme);

    let currentFrequency = 0;

    let dataSource = {
        chart: {
            bgColor: "#080e21",
            caption: "CPU Usage",
            lowerLimit: "0.00",
            upperLimit: "8.00",
            numberSuffix: "Mhz",
            theme: "fusion",
            baseFontSize: "11",
            baseFontColor: "#ffffff",
            showToolTip: "1",
            toolTipBgColor: "#666666",
            toolTipBgAlpha: "80",
            pivotFillColor: "#ffffff",
            toolbarButtonColor: "#d90000",
            showHoverEffect: "1",
            dialbgHoverColor: "#d90000",
            gaugeBorderColor: "#ffffff",
            gaugeBorderThickness: "4",
            showValue: "1",
            valueFontColor: "#ffffff",
            valueFontSize: "14",
            baseFontSize: "12",
        },
        colorRange: {
            color: [
                {
                    minValue: "0",
                    maxValue: "2",
                    code: "#ff7a7a",
                },
                {
                    minValue: "2",
                    maxValue: "4",
                    code: "#ff4d4d",
                },
                {
                    minValue: "4",
                    maxValue: "6",
                    code: "#fc2828",
                },
                {
                    minValue: "6",
                    maxValue: "8",
                    code: "#820000",
                },
            ],
        },
        dials: {
            dial: [
                {
                    value: currentFrequency,
                    bgColor: "#ffffff",
                },
            ],
        },
    };
    let chartConfig = {
        type: "angulargauge",
        width: "914",
        height: "360",
        renderAt: "chart-container",
        dataSource,
    };

    onMount(async () => {
        let systemCpuInfo = await GetSystemCpu();
        currentFrequency = systemCpuInfo.currentFrequency.replace("Mhz", "");

        const UpdateHandler = () => {
            let dataSource = chartConfig.dataSource;
            dataSource.dials.dial[0].value = currentFrequency;
            chartConfig = { ...chartConfig, dataSource };
        };

        UpdateHandler();

        setInterval(async () => {
            systemCpuInfo = await GetSystemCpu();
            currentFrequency = systemCpuInfo.currentFrequency.replace(
                "Mhz",
                ""
            );

            UpdateHandler();
        }, 750);
    });
</script>

<div class="m-2 border-2 rounded relative">
    <SvelteFC {...chartConfig} />
    <RemoveTrialText />
</div>
