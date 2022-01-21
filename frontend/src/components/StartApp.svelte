<script>
    import Fa from "svelte-fa";
    import {
        faCheckCircle,
        faTimesCircle,
        faSpinner,
    } from "@fortawesome/free-solid-svg-icons";
    import { slide } from "svelte/transition";
    import { toast } from "@zerodevx/svelte-toast";

    import StartApp from "../api/StartApp/StartApp";

    let inputValue;
    let pingStatus = "stopped";
    let error = [];

    $: inputValue == "" ? (pingStatus = "stopped") : null;

    const handleSubmit = async () => {
        error = [];
        if (!inputValue) {
            error.message = "Please enter a application name";
            return;
        }
        //if inputValue has space or ';' in it then it will error
        if (
            inputValue.includes(" ") ||
            inputValue.includes(";") ||
            inputValue.includes("sudo")
        ) {
            error.message = "Please enter a valid application name";
            return;
        }

        pingStatus = "pending";
        const res = await StartApp(inputValue);
        console.log(res);
        res === "successful"
            ? (pingStatus = "success")
            : (pingStatus = "error");
    };
</script>

<div class="border-2 rounded m-2 flex flex-col gap-3 p-3">
    <div class="text-center font-bold mt-2">Start App</div>
    {#if error.message}
        <div transition:slide class="text-red-500 text-center">
            {error.message}
        </div>
    {/if}
    <div class="grid grid-cols-12 gap-3 m-3">
        <form on:submit|preventDefault={handleSubmit} class="col-span-8">
            <input
                bind:value={inputValue}
                type="text"
                class="p-3 rounded w-full text-gray-700"
                placeholder="Type an application name"
            />
            <div class="text-black" />
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
                class={`text-white bg-green-400 rounded p-3 w-full`}
                >Start</button
            >
        </div>
    </div>
</div>
