<script>
    import Fa from "svelte-fa";
    import {
        faCheckCircle,
        faTimesCircle,
        faSpinner,
    } from "@fortawesome/free-solid-svg-icons";

    import PingControl from "../api/PingControl/PingControl";

    let inputValue;
    let pingStatus = "stopped";

    $: inputValue == "" ? (pingStatus = "stopped") : null;

    const handleSubmit = async () => {
        if (!inputValue) {
            alert("Please enter a valid IP address or domain name");
            return;
        }
        pingStatus = "pending";
        const res = await PingControl(inputValue);
        res == "Up" ? (pingStatus = "success") : (pingStatus = "error");
    };
</script>

<div class="border-2 rounded m-2 flex flex-col gap-3 p-3">
    <div class="text-center font-bold mt-2">Ping Control</div>
    <div class="grid grid-cols-12 gap-3 m-3">
        <form on:submit|preventDefault={handleSubmit} class="col-span-8">
            <input
                bind:value={inputValue}
                type="text"
                class="p-3 rounded w-full text-gray-700"
                placeholder="Type a domain or an Ip address"
            />
        </form>
        <div class="col-span-1 mx-auto items-center mt-1">
            {#if pingStatus == "pending"}
                <Fa spin icon={faSpinner} size="2x" />
            {:else if pingStatus == "success"}
                <Fa color="green" icon={faCheckCircle} size="2x" />
            {:else if pingStatus == "error"}
                <Fa color="red" icon={faTimesCircle} size="2x" />
            {/if}
        </div>
        <div class="col-span-3">
            <button
                on:click={handleSubmit}
                class="text-white bg-green-400 rounded p-3 w-full">Check</button
            >
        </div>
    </div>
</div>
