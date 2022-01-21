<script>
    import { onMount } from "svelte";

    import WorkingApps from "../api/WorkingAppsComponent/GetWorkingApps";

    let workingApps = [];
    onMount(async () => {
        workingApps = await WorkingApps();

        //if working apps has same app remove it
        for (let i = 0; i < workingApps.length; i++) {
            for (let j = 0; j < workingApps.length; j++) {
                if (i != j) {
                    if (workingApps[i] == workingApps[j]) {
                        workingApps.splice(j, 1);
                    }
                }
            }
        }
    });
</script>

<div
    class="border-2 m-2 text-center rounded max-h-72 h-72 overflow-scroll relative"
>
    <div class="border-b font-bold text-base p-2">Working Apps</div>
    <div class="grid grid-cols-4 gap-2 m-3">
        {#each workingApps as app, i}
            <span
                class="p-1 font-semibold bg-red-700 opacity-60 capitalize hover:opacity-100 cursor-default transition duration-300 text-white rounded-lg"
                >{app}</span
            >
        {/each}
    </div>
</div>
