<script>
    import { onMount } from "svelte";

    import Widgets from "fusioncharts/fusioncharts.widgets";

    //Import the theme as fusion
    import FusionTheme from "fusioncharts/themes/fusioncharts.theme.fusion";

    //Import the Svelte component
    import SvelteFC, { fcRoot } from "svelte-fusioncharts";
    import RemoveTrialText from "../tools/removeTrialText.svelte";

    // Always set FusionCharts as the first parameter
    fcRoot(FusionCharts, Widgets, FusionTheme);

    export let gpuInfo = [];

    let chartConfigs = [];

    onMount(() => {
        console.log(gpuInfo);

        const renderComponent = () => {
            for (let i = 0; i < gpuInfo.length; i++) {
                chartConfigs = [
                    ...chartConfigs,
                    {
                        type: "vled",
                        width: 574,
                        height: 200,
                        dataFormat: "json",
                        dataSource: {
                            chart: {
                                upperlimit: gpuInfo[i].gpuTotalTemory,
                                numbersuffix: " mb",
                                showvalue: "0",
                                chartbottommargin: "50",
                                ledgap: "1",
                                theme: "fusion",
                                bgColor: "#080E21",
                                baseFontColor: "#ffffff",
                                showToolTip: "1",
                                toolTipBgColor: "#666666",
                                toolTipBgAlpha: "80",
                                lowerLimit: "0",
                                upperLimit: gpuInfo[i].gpuTotalTemory,
                            },
                            colorrange: {
                                color: [
                                    {
                                        minValue: "0",
                                        maxValue:
                                            gpuInfo[i].gpuTotalTemory * 0.3,
                                        code: "#ffbaba",
                                    },
                                    {
                                        minValue:
                                            gpuInfo[i].gpuTotalTemory * 0.3,
                                        maxValue:
                                            gpuInfo[i].gpuTotalTemory * 0.7,
                                        code: "#d45353",
                                    },
                                    {
                                        minValue:
                                            gpuInfo[i].gpuTotalTemory * 0.7,
                                        maxValue: gpuInfo[i].gpuTotalTemory,
                                        code: "#db0000",
                                    },
                                ],
                            },
                            value: gpuInfo[i].gpuUsedMemory,
                        },
                    },
                ];
            }
        };
        renderComponent();

        setInterval(() => {
            renderComponent();
        }, 5000);
    });

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
</script>

<div class="flex flex-col">
    {#each gpuInfo as _gpu, i}
        <SvelteFC {...chartConfigs[i]} />
    {/each}
</div>
