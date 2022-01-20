<script>
    import { onMount } from "svelte";

    import GetCurrentUser from "../api/GeneralSystemInfoComponent/GetCurrentUser";
    import GetIpAddress from "../api/GeneralSystemInfoComponent/GetIpAddress";
    import GetSystemBootInfo from "../api/GeneralSystemInfoComponent/GetSystemBootInfo";
    import GetSystemInfo from "../api/GeneralSystemInfoComponent/GetSystemInfo";

    let currentUser, systemBootInfo, systemInfo, ipAddress;
    onMount(async () => {
        currentUser = await GetCurrentUser();
        systemBootInfo = await GetSystemBootInfo();
        systemInfo = await GetSystemInfo();
        ipAddress = await GetIpAddress();
    });

    const tableHeaders = [
        "Username",
        "Ip Address",
        "OS",
        "Distro",
        "Release",
        "Working Since",
    ];
</script>

<div class="text-center  border m-2 p-3">
    <div class="grid grid-cols-6">
        {#each tableHeaders as header}
            <div class="border-b font-bold text-sm uppercase w-1/2 mx-auto">
                {header}
            </div>
        {/each}
    </div>
    <div class="grid grid-cols-6 text-sm">
        <div>{currentUser}</div>
        <div>{ipAddress}</div>
        <div>{systemInfo?.system}</div>
        <div>{systemInfo?.nodeName}</div>
        <div>{systemInfo?.release}</div>
        <div>{systemBootInfo}</div>
    </div>
</div>
