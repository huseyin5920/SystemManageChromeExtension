<script>
    import { onMount } from "svelte/internal";

    //SECTION: SOCKET

    const JournalSocket = new WebSocket("ws://192.168.30.72:8766");

    let allJournalDatas = [];

    let tableRef;

    $: if (allJournalDatas.length > 50) {
        allJournalDatas.shift();
    }

    JournalSocket.onopen = function () {
        JournalSocket.send("Hello");
    };

    JournalSocket.onmessage = function (event) {
        //console.log(event);
        allJournalDatas = [...allJournalDatas, event.data];
        if (tableRef) {
            tableRef.scrollTop = tableRef.scrollHeight;
        }
    };

    JournalSocket.onclose = function () {
        console.log("Network socket closed");
    };

    JournalSocket.onerror = function (error) {
        console.log(error);
    };

    //!SECTION
</script>

<div
    bind:this={tableRef}
    class="border-2 rounded m-2 flex flex-col snap-y gap-3 p-3 h-[18.75rem] max-h-[18.75rem] overflow-auto"
>
    {#each allJournalDatas as journalData}
        <div>
            <code>
                {journalData}
            </code>
        </div>
    {/each}
</div>
