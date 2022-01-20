<script>
    import Fa from "svelte-fa";
    import {
        faCheckCircle,
        faTimesCircle,
        faSpinner,
    } from "@fortawesome/free-solid-svg-icons";

    import CheckProcessInfo from "../api/CheckProcessInfoComponent/CheckProcessInfo";

    let inputValue;
    let processStatus = "stopped";

    $: inputValue == "" ? (processStatus = "stopped") : null;

    const handleSubmit = async () => {
        if (!inputValue) {
            alert("Please enter a process name");
            return;
        }
        processStatus = "pending";
        const res = await CheckProcessInfo(inputValue);
        console.log(res);
        typeof res === "string"
            ? (processStatus = "error")
            : (processStatus = "success");
    };
</script>

<div class="border-2 rounded m-2 flex flex-col gap-3 p-3">
    <div class="text-center font-bold mt-2">Check Process</div>
    <div class="grid grid-cols-12 gap-3 m-3">
        <form on:submit|preventDefault={handleSubmit} class="col-span-8">
            <input
                bind:value={inputValue}
                type="text"
                class="p-3 rounded w-full text-gray-700"
                placeholder="Type a process name"
            />
        </form>
        <div class="col-span-1 mx-auto items-center mt-1">
            {#if processStatus == "pending"}
                <Fa spin icon={faSpinner} size="2x" />
            {:else if processStatus == "success"}
                <Fa color="green" icon={faCheckCircle} size="2x" />
            {:else if processStatus == "error"}
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
