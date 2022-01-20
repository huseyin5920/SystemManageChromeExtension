<script>
    import { onMount } from "svelte";

    import RemoveTrialText from "./tools/removeTrialText.svelte";

    //SECTION: SOCKET

    const networkSocket = new WebSocket("ws://localhost:8765");

    let liveNetworkdata;

    let network1, network2, network3, network4;

    networkSocket.onopen = function () {
        setInterval(() => {
            networkSocket.send("Hello World");
        }, 1000);
    };

    networkSocket.onmessage = function (event) {
        liveNetworkdata = JSON.parse(event.data);
        console.log(liveNetworkdata);
        network1 = Math.floor(liveNetworkdata?.wlp2s0[0] / 1024000);
        network2 = Math.floor(liveNetworkdata?.wlp2s0[1] / 1024000);
        network3 = Math.floor(liveNetworkdata?.wlp2s0[2] / 1024000);
        network4 = Math.floor(liveNetworkdata?.wlp2s0[3] / 1024000);

        //console.log(network1, network2, network3, network4);

        var d = new Date();

        dataSource.categories[0].category = [
            ...dataSource.categories[0].category,
            {
                //if seconds are less than 10, add a 0 before the number

                label:
                    (d.getHours() < 10 ? "0" + d.getHours() : d.getHours()) +
                    ":" +
                    (d.getMinutes() < 10
                        ? "0" + d.getMinutes()
                        : d.getMinutes()) +
                    ":" +
                    (d.getSeconds() < 10
                        ? "0" + d.getSeconds()
                        : d.getSeconds()),
            },
        ];
        if (dataSource.categories[0].category.length > 10) {
            dataSource.categories[0].category.shift();
        }

        dataSource.dataset[0].data = [
            ...dataSource.dataset[0].data,
            { value: network1 },
        ];

        dataSource.dataset[1].data = [
            ...dataSource.dataset[1].data,
            { value: network2 },
        ];

        dataSource.dataset[2].data = [
            ...dataSource.dataset[2].data,
            { value: network3 },
        ];

        dataSource.dataset[3].data = [
            ...dataSource.dataset[3].data,
            { value: network4 },
        ];

        dataSource = dataSource;
        //console.log(dataSource.categories);
    };

    networkSocket.onclose = function () {
        console.log("Network socket closed");
    };

    networkSocket.onerror = function (error) {
        console.log(error);
    };

    //!SECTION

    import FusionCharts from "fusioncharts";
    import Widgets from "fusioncharts/fusioncharts.widgets";
    import FusionTheme from "fusioncharts/themes/fusioncharts.theme.fusion";
    import SvelteFC, { fcRoot } from "svelte-fusioncharts";

    fcRoot(FusionCharts, Widgets, FusionTheme);

    $: dataSource = {
        chart: {
            caption: "Live Network Data",
            numberSuffix: " bytes",
            numdisplaysets: "10",
            labeldisplay: "rotate",
            showRealTimeValue: "0",
            realTimeValueSep: " | ",
            theme: "fusion",
            plotToolText: "$label<br> <b>$dataValue</b>",
            setAdaptiveYMin: "1",
            valueFontColor: "#ffffff",
            valueFontSize: "14",
            baseFontSize: "12",
            baseFontColor: "#ffffff",
            toolbarButtonColor: "#d90000",
            toolTipBgColor: "#666666",
            toolTipBgAlpha: "80",
            showHoverEffect: "1",
            bgColor: "#080e21",
            xaxisname: "Time",
            slantlabels: "1",
            setadaptiveymin: "1",
            setadaptivesymin: "1",
        },
        categories: [
            {
                category: [],
            },
        ],
        dataset: [
            {
                data: [],
            },
            {
                data: [],
            },
            {
                data: [],
            },
            {
                data: [],
            },
        ],
    };

    $: chartConfigs = {
        type: "realtimeline",
        width: 618,
        height: 300,
        dataFormat: "json",

        dataSource,
    };
</script>

<div class="m-2 border-2 rounded relative">
    <SvelteFC {...chartConfigs} />
    <RemoveTrialText />
</div>
