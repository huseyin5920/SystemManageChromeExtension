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

    let gpuInfo = [];

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

    onMount(async () => {
        const renderComponent = async () => {
            gpuInfo = await GetSystemGpu();
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
                                gaugeFillColor: returnColor(
                                    gpuInfo[i].gpuTemperature
                                ).textColor,
                                showToolTip: "1",
                                toolTipBgColor: "#666666",
                                toolTipBgAlpha: "80",
                                showValue: "1",
                                valueFontColor: returnColor(
                                    gpuInfo[i].gpuTemperature
                                ).textColor,
                                valueFontSize: "14",
                            },
                            value: gpuInfo[i].gpuTemperature,
                        },
                    },
                ];

                chartConfigs[i].dataSource.value = gpuInfo[i].gpuTemperature;
                chartConfigs[i].dataSource.value = gpuInfo[i].gpuTemperature;
                chartConfigs[i].dataSource.chart.gaugeFillColor = returnColor(
                    gpuInfo[i].gpuTemperature
                ).textColor;
                chartConfigs[i].dataSource.chart.valueFontColor = returnColor(
                    gpuInfo[i].gpuTemperature
                ).textColor;
            }
        };
        renderComponent();

        setInterval(async () => {
            renderComponent();
        }, 5000);
    });
</script>

<div class="border-2 rounded m-2 gpu_container overflow-scroll">
    {#if gpuInfo.length > 0}
        {#each gpuInfo as gpu, i}
            <div class="text-center ">{gpuInfo[i].gpuName}</div>
            <div class="relative flex">
                <SvelteFC {...chartConfigs[i]} />
                <RemoveTrialText />
                <RealTimeGpuUsage {gpuInfo} />
            </div>
        {/each}
    {:else}
        <div class="text-center mt-2 text-2xl">No GPU found</div>
    {/if}
</div>

<style>
    .gpu_container {
        height: 228px;
        max-height: 228px;
    }
</style>
