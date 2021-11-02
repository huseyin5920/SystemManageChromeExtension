<script>
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
</script>

<table>
  <tr>
    {#each tableList as item}
      <th>{item}</th>
    {/each}
  </tr>
  {#each cpuData as cpu}
    <tr>
      <td>{cpu.PID}</td>
      <td>{cpu.USER}</td>
      <td>{cpu.PR}</td>
      <td>{cpu.NI}</td>
      <td>{cpu.VIRT}</td>
      <td>{cpu.RES}</td>
      <td>{cpu.SHR}</td>
      <td>{cpu.CPU}</td>
      <td>{cpu.MEM}</td>
      <td>{cpu.TIME}</td>
      <td>{cpu.COMMAND}</td>
    </tr>
  {/each}
</table>

<!-- <style>
  td {
    justify-items: center;
    padding: 45px;
  }
</style> -->
