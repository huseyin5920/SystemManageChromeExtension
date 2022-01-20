<script>
    import { onMount } from "svelte";

    import GetFirewallStatus from "../api/FirewallComponent/firewallStatus";

    onMount(async () => {
        console.log("asdasd");
        const response = await GetFirewallStatus();
        console.log(response);
    });
</script>
