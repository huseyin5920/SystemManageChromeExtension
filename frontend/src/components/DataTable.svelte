<script>
  import { onMount } from "svelte";

  import GetCpu from "../api/getCpu";
  import GetMemory from "../api/getMemory";

  import Fa from "svelte-fa";
  import { faFlag } from "@fortawesome/free-solid-svg-icons";

  let tableData = [];
  onMount(() => {
    setInterval(async () => {
      tableData = await GetCpu();
    }, 1000);
    tableData = tableData;
  });

  $: console.log(tableData);

  const tableList = [
    { name: "PID", isSelected: false },
    { name: "USER", isSelected: false },
    { name: "PR", isSelected: false },
    { name: "NI", isSelected: false },
    { name: "VIRT", isSelected: false },
    { name: "RES", isSelected: false },
    { name: "SHR", isSelected: false },
    { name: "CPU", isSelected: true },
    { name: "MEM", isSelected: false },
    { name: "TIME", isSelected: false },
    { name: "COMMAND", isSelected: false },
  ];

  const selectTypeOfData = (el) => {
    tableList.forEach((item) => {
      item.isSelected = false;
    });
    el.isSelected = true;

    tableList = tableList;
  };
</script>

<div class="border rounded m-5 w-3/5 shadow-2xl text-center">
  <div class="grid grid-cols-11 border-b-2 p-2 font-bold text-xs">
    {#each tableList as el}
      {#if el.name == "MEM" || el.name == "CPU"}
        <div
          class:bg-gray-200={el.isSelected}
          on:click={() => selectTypeOfData(el)}
          class="text-center cursor-pointer"
        >
          <span>{el.name}</span>
        </div>
      {:else}
        <div>{el.name}</div>
      {/if}
    {/each}
  </div>
  <div class="text-xs">
    {#each tableData as data}
      <div class="grid grid-cols-11 border-b-2 p-2 max-h-8 overflow-hidden">
        <div>{data.PID}</div>
        <div>{data.USER}</div>
        <div>{data.PR}</div>
        <div>{data.NI}</div>
        <div>{data.VIRT}</div>
        <div>{data.RES}</div>
        <div>{data.SHR}</div>
        <div>{data.CPU}</div>
        <div>{data.MEM}</div>
        <div>{data.TIME}</div>
        <div>{data.COMMAND}</div>
      </div>
    {/each}
  </div>
</div>
