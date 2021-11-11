<script>
    import { onMount } from "svelte";
    import GetSystemLiveCpuInfo from "../../api/SystemLiveCpuInfoComponent/getSystemLiveCpuInfo";

    import FusionCharts from "fusioncharts";
    import Charts from "fusioncharts/fusioncharts.charts";
    import FusionTheme from "fusioncharts/themes/fusioncharts.theme.fusion";
    import SvelteFC, { fcRoot } from "svelte-fusioncharts";
    import TotalCpuInfo from "./TotalCpuInfo.svelte";
    import RemoveTrialText from "../tools/removeTrialText.svelte";

    fcRoot(FusionCharts, Charts, FusionTheme);

    let cpuData = {};

    let chartConfigs = [];

    const returnColor = (value) => {
        if (value >= 80) {
            return { textColor: "#8c0000", bgColor: "#fff" };
        }
        if (value >= 60) {
            return { textColor: "#db0000", bgColor: "#fff" };
        }
        if (value >= 40) {
            return { textColor: "#ff4242", bgColor: "#fff" };
        }
        if (value >= 20) {
            return { textColor: "#e36f6f", bgColor: "#000" };
        }
        if (value >= 0) {
            return { textColor: "#ffb8b8", bgColor: "#000" };
        }
    };

    onMount(async () => {
        const renderComponent = async () => {
            cpuData = await GetSystemLiveCpuInfo();

            for (let i = 0; i < cpuData.cores.length; i++) {
                chartConfigs = [
                    ...chartConfigs,
                    {
                        type: "cylinder",
                        width: 180,
                        height: 190,
                        dataFormat: "json",
                        dataSource: {
                            chart: {
                                bgColor: "#080E21",
                                baseFontColor: "#ffffff",
                                caption: `Core ${i + 1}`,
                                lowerlimit: "0",
                                upperlimit: "100",
                                lowerlimitdisplay: "0",
                                upperlimitdisplay: "100",
                                numbersuffix: " %",
                                cylfillcolor: returnColor(cpuData.cores[i])
                                    .textColor,
                                theme: "fusion",
                                showToolTip: "1",
                                toolTipBorderColor: "#666666",
                                toolTipBgColor: returnColor(cpuData.cores[i])
                                    .bgColor,
                                toolTipBgAlpha: "80",
                                cylGlassColor: returnColor(cpuData.cores[i])
                                    .textColor,
                                cylRadius: "25",
                                cylYScale: "25",
                                showValue: "1",
                                valueFontColor: returnColor(cpuData.cores[i])
                                    .textColor,
                                valueFontSize: "14",
                            },
                            value: `${cpuData.cores[i]}`,
                        },
                    },
                ];

                chartConfigs[i].dataSource.value = cpuData.cores[i];

                chartConfigs[i].dataSource.chart.cylfillcolor = returnColor(
                    cpuData.cores[i]
                ).textColor;
                chartConfigs[i].dataSource.chart.toolTipBgColor = returnColor(
                    cpuData.cores[i]
                ).bgColor;
                chartConfigs[i].dataSource.chart.cylGlassColor = returnColor(
                    cpuData.cores[i]
                ).textColor;
                chartConfigs[i].dataSource.chart.valueFontColor = returnColor(
                    cpuData.cores[i]
                ).textColor;
            }
        };

        renderComponent();

        setInterval(async () => {
            renderComponent();
        }, 1000);
    });
</script>

<div class="m-2 border-2 rounded test relative">
    {#if cpuData.cores}
        <div class=" grid grid-cols-4 gap-x-9">
            {#each cpuData.cores as _core, i}
                <div class="relative">
                    <SvelteFC {...chartConfigs[i]} />
                    <RemoveTrialText />
                </div>
            {/each}
            <div class="col-span-4">
                <TotalCpuInfo totalCpuInfo={cpuData.totalCpu} {returnColor} />
            </div>
        </div>
    {:else}
        <div class="skeleton mx-auto text-center animate-pulse">
            <div class="font-extrabold text-6xl mt-24">Loading...</div>
        </div>
    {/if}
</div>

<style>
    .skeleton {
        height: 534px;
    }
</style>
