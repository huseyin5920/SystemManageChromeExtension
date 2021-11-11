<script>
    import { onMount } from "svelte";
    import GetSystemLiveCpuInfo from "../../api/SystemLiveCpuInfoComponent/getSystemLiveCpuInfo";

    export let totalCpuInfo, returnColor;

    import FusionCharts from "fusioncharts";
    import Charts from "fusioncharts/fusioncharts.charts";
    import FusionTheme from "fusioncharts/themes/fusioncharts.theme.fusion";
    import SvelteFC, { fcRoot } from "svelte-fusioncharts";
    import RemoveTrialText from "../tools/removeTrialText.svelte";

    // Always set FusionCharts as the first parameter
    fcRoot(FusionCharts, Charts, FusionTheme);

    const chartConfigs = {
        type: "hled",
        id: "myGauge",
        renderAt: "chart-container",
        width: "904.5",
        height: "150",
        dataFormat: "json",
        dataSource: {
            chart: {
                bgColor: "#080e21",
                caption: "Total Cpu Usage",
                baseFontColor: "#ffffff",
                lowerLimit: "0",
                upperLimit: "100",
                numbersuffix: " %",
                chartTopMargin: "20",
                chartBottomMargin: "40",
                theme: "fusion",
                valueFontColor: returnColor(totalCpuInfo).textColor,
            },
            colorRange: {
                color: [
                    {
                        minValue: "0",
                        maxValue: "25",
                        code: "#ffa8a8",
                    },
                    {
                        minValue: "25",
                        maxValue: "50",
                        code: "#ff7373",
                    },
                    {
                        minValue: "50",
                        maxValue: "75",
                        code: "#ff3838",
                    },
                    {
                        minValue: "75",
                        maxValue: "100",
                        code: "#ff0000",
                    },
                ],
            },
            value: totalCpuInfo,
        },
    };

    onMount(() => {
        setInterval(() => {
            chartConfigs.dataSource.value = totalCpuInfo;
            chartConfigs.dataSource.chart.cylfillcolor =
                returnColor(totalCpuInfo).textColor;
            chartConfigs.dataSource.chart.toolTipBgColor =
                returnColor(totalCpuInfo).bgColor;
            chartConfigs.dataSource.chart.valueFontColor =
                returnColor(totalCpuInfo).textColor;
        }, 1000);
    });
</script>

<div class="relative">
    <SvelteFC {...chartConfigs} />
    <RemoveTrialText />
</div>
