<script>
  import CheckProcessInfo from "./components/CheckProcessInfo.svelte";

  import CpuMemoryDataTable from "./components/CpuMemoryDataTable.svelte";
  import DiskUsage from "./components/DiskUsage.svelte";
  import Firewall from "./components/Firewall.svelte";
  import GeneralSystemInfo from "./components/GeneralSystemInfo.svelte";
  import LiveNetworkTraffic from "./components/LiveNetworkTraffic.svelte";
  import PingControl from "./components/PingControl.svelte";
  import SystemCpuInfo from "./components/SystemCpuInfo.svelte";
  import SystemGpuInfo from "./components/SystemGpuInfo/SystemGpuInfo.svelte";
  import SystemLiveCpuInfo from "./components/SystemLiveCpuInfo/SystemLiveCpuInfo.svelte";
  import SystemNetworkInfo from "./components/SystemNetworkInfo.svelte";
  import Users from "./components/Users.svelte";
</script>

<div class="grid grid-cols-12 text-white">
  <div class="col-span-12">
    <GeneralSystemInfo />
  </div>
  <div class="col-span-6">
    <CpuMemoryDataTable />
  </div>
  <div class="col-span-6">
    <SystemCpuInfo />
  </div>
  <div class="col-span-6">
    <SystemLiveCpuInfo />
  </div>

  <div>
    <Users />
  </div>
  <div class="col-span-5 h-auto flex flex-col">
    <SystemNetworkInfo />
    <SystemGpuInfo />
  </div>
  <div class="col-span-4">
    <div class="flex flex-col">
      <PingControl />
      <CheckProcessInfo />
    </div>
  </div>
  <div class="col-span-4">
    <DiskUsage />
  </div>
  <div class="col-span-4">
    <LiveNetworkTraffic />
  </div>
</div>

<style global>
  @tailwind base;
  @tailwind components;
  @tailwind utilities;

  :global(body) {
    font-family: "Inter", sans-serif;
    background: #080e21;
    background-repeat: no-repeat;
    height: 100%;
    background-attachment: fixed;
    margin: 0;
  }

  /* For removing FusionCharts Trial Text  */

  ::-webkit-scrollbar {
    width: 4px;
    height: 4px;
  }
  ::-webkit-scrollbar-button {
    width: 0px;
    height: 0px;
  }
  ::-webkit-scrollbar-thumb {
    background: #e1e1e1;
    border: 0px none #ffffff;
    border-radius: 50px;
  }
  ::-webkit-scrollbar-thumb:hover {
    background: #ffffff;
  }
  ::-webkit-scrollbar-thumb:active {
    background: #000000;
  }
  ::-webkit-scrollbar-track {
    background: #666666;
    border: 0px none #ffffff;
    border-radius: 54px;
  }
  ::-webkit-scrollbar-track:hover {
    background: #666666;
  }
  ::-webkit-scrollbar-track:active {
    background: #333333;
  }
  ::-webkit-scrollbar-corner {
    background: transparent;
  }
</style>
