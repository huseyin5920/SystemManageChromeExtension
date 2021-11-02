<script>
<<<<<<< HEAD
  import DataTable from "./components/DataTable.svelte";
=======
  import { onMount } from "svelte";
  import GetMemory from "./api/getMemory";
  import GetCpu from "./api/getCpu";

  let memoryData;
  let cpuData = [];
  onMount(() => {
    setInterval(async () => {
      memoryData = await GetMemory();
      cpuData = await GetCpu();
    }, 3000);
    cpuData = cpuData;
  });
  $: console.log(cpuData);

  const tableList = [
    "PID",
    "USER",
    "PR",
    "NI",
    "VIRT",
    "RES",
    "SHR",
    "CPU",
    "MEM",
    "TIME",
    "COMMAND",
  ];
>>>>>>> b321cfd28efa1cc46f355a85a5f396d39dadfb28
</script>

<DataTable />

<style global>
  @tailwind base;
  @tailwind components;
  @tailwind utilities;
</style>
