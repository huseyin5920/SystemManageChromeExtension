<script>
    import { onMount } from "svelte";

    import GetSystemGpu from "../../api/SystemGpuInfoComponent/getSystemGpu";

    import Widgets from "fusioncharts/fusioncharts.widgets";

    //Import the theme as fusion
    import FusionTheme from "fusioncharts/themes/fusioncharts.theme.fusion";

    //Import the Svelte component
    import SvelteFC, { fcRoot } from "svelte-fusioncharts";
    import RemoveTrialText from "../tools/removeTrialText.svelte";
    import RealTimeGpuUsage from "./RealTimeGpuUsage.svelte";

    // Always set FusionCharts as the first parameter
    fcRoot(FusionCharts, Widgets, FusionTheme);

    let gpuInfo = [
        {
            gpId: 0,
            gpuFreeMemory: 2002.0,
            gpuLoad: 0.0,
            gpuName: "NVIDIA GeForce MX330",
            gpuTemperature: 53.0,
            gpuTotalTemory: 2002.0,
            gpuUsedMemory: 0.0,
            gpuUuid: "GPU-96a08d91-2cbc-22e3-e3de-2901658733f5",
        },
    ];

    let chartConfigs = [];

    const returnColor = (value) => {
        if (value >= 80) {
            return { textColor: "#bf0000", bgColor: "#fff" };
        }
        if (value >= 60) {
            return { textColor: "#c23434", bgColor: "#fff" };
        }
        if (value >= 40) {
            return { textColor: "#c95b5b", bgColor: "#fff" };
        }
        if (value >= 20) {
            return { textColor: "#ffa1a1", bgColor: "#000" };
        }
        if (value >= 0) {
            return { textColor: "#80d9ff", bgColor: "#000" };
        }
    };

    for (let i = 0; i < gpuInfo.length; i++) {
        chartConfigs = [
            ...chartConfigs,
            {
                type: "thermometer", // The gauge type
                width: "200", // Width of the gauge
                height: "200", // Height of the gauge
                dataFormat: "json", // Data type
                renderAt: "chart-container", //Container where the gauge will render
                dataSource: {
                    // Gauge Configuration
                    chart: {
                        lowerLimit: "0",
                        upperLimit: "100",
                        numberSuffix: "°C",
                        theme: "fusion",
                        bgColor: "#080E22",
                        baseFontColor: "#ffffff",
                        gaugeFillColor: returnColor(gpuInfo[i].gpuTemperature)
                            .textColor,
                        /* showToolTip: "1",
                        toolTipBorderColor: "#666666",
                        toolTipBgColor: returnColor(gpuInfo[i].gpuTemperature)
                            .bgColor,
                        toolTipBgAlpha: "80", */
                        showValue: "1",
                        valueFontColor: returnColor(gpuInfo[i].gpuTemperature)
                            .textColor,
                        valueFontSize: "14",
                    },
                    value: gpuInfo[i].gpuTemperature,
                },
            },
        ];
    }

    onMount(async () => {
        /* gpuInfo = await GetSystemGpu(); */
    });
</script>

<div class="border-2 rounded m-2 gpu_container overflow-scroll">
    {#each gpuInfo as gpu, i}
        <div class="text-center ">{gpuInfo[i].gpuName}</div>
        <div class="relative flex">
            <SvelteFC {...chartConfigs[i]} />
            <RemoveTrialText />
            <RealTimeGpuUsage {gpuInfo} />
        </div>
    {/each}
</div>

<style>
    .gpu_container {
        height: 228px;
        max-height: 228px;
    }
</style>
