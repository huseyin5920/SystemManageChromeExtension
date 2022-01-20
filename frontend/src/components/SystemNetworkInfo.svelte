<script>
    import { onMount } from "svelte";

    import GetSystemNetworkInfo from "../api/SystemNetworkInfoComponent/getSystemNetworkInfo";

    let networkData = [];
    onMount(async () => {
        networkData = await GetSystemNetworkInfo();
    });

    const tableHeaders = ["Address", "Broadcast", "Netmask"];
</script>

<div class="border-2 m-2 text-center rounded max-h-72 overflow-scroll relative">
    <div class="border-b font-bold text-base p-2">System Network</div>
    <div
        class="grid grid-cols-3 border-b border-gray-400 p-2 font-bold text-sm"
    >
        {#each tableHeaders as header}
            <div>{header}</div>
        {/each}
    </div>
    <div>
        {#each networkData as data, i}
            <div
                class="grid grid-cols-3 p-1 text-sm"
                class:border-b={i != networkData.length - 1}
            >
                <div>{data.address}</div>
                <div>
                    {data.broadcast == null ? "--------" : data.broadcast}
                </div>
                <div>{data.netmask}</div>
            </div>
        {/each}
    </div>
</div>
