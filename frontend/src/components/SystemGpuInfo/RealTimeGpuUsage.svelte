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
    });
</script>

{#each gpuInfo as gpu, i}
    <SvelteFC {...chartConfigs[i]} />
{/each}
