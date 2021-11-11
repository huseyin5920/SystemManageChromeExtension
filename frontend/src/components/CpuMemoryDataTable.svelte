<script>
  import { onMount } from "svelte";

  import GetCpu from "../api/CpuMemoryComponent/getCpu";
  import GetMemory from "../api/CpuMemoryComponent/getMemory";

  import Fa from "svelte-fa";
  import { faMinusCircle } from "@fortawesome/free-solid-svg-icons";

  let tableData = [];
  let interval;
  onMount(async () => {
    tableData = await GetCpu();
    interval = setInterval(async () => {
      tableData = await GetCpu();
    }, 3000);
    tableData = tableData;
  });

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

  const selectTypeOfData = async (el) => {
    clearInterval(interval);
    el.name === "CPU"
      ? (tableData = await GetCpu())
      : (tableData = await GetMemory());
    interval = setInterval(async () => {
      el.name === "CPU"
        ? (tableData = await GetCpu())
        : (tableData = await GetMemory());
    }, 3000);

    tableList.forEach((item) => {
      item.isSelected = false;
    });
    el.isSelected = true;

    tableList = tableList;
  };

  const killProcess = async (pid) => {
    console.log(pid);
  };
</script>

<div class="border-2 rounded m-2 shadow-2xl text-center">
  <div class=" grid grid-cols-12 border-b-2 p-2 font-bold text-xs">
    {#each tableList as el}
      {#if el.name == "MEM" || el.name == "CPU"}
        <div
          class:border-b-2={el.isSelected}
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
    {#each tableData as data, i}
      <div
        class:border-b-2={i != tableData.length - 1}
        class="grid grid-cols-12  p-2 max-h-8 overflow-hidden text-center items-center"
      >
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
        <div>
          {data.COMMAND.length > 10
            ? `${data.COMMAND.substr(0, 7)}...`
            : data.COMMAND}
        </div>
        <div
          on:click={() => killProcess(data.PID)}
          class="text-red-600 cursor-pointer mx-auto"
        >
          <Fa size="16" icon={faMinusCircle} />
        </div>
      </div>
    {/each}
  </div>
</div>
