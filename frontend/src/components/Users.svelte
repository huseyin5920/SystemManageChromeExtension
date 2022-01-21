<script>
    import { onMount } from "svelte";

    import GetAllUsers from "../api/UsersComponent/getAllUsers";

    let allUsers = [];
    onMount(async () => {
        allUsers = await GetAllUsers();

        allUsers = Object.keys(allUsers).map((key) => allUsers[key]);
    });
</script>

<div
    class="relative flex flex-col border-2 p-2 m-2 users overflow-x-hidden overflow-y-visible rounded"
>
    <div class="text-center font-bold">All Users</div>
    {#each allUsers as user}
        <div class="p-1 border border-r-0 border-l-0 border-gray-500">
            {user}
        </div>
    {/each}
</div>

<style>
    .users {
        height: 534px;
    }
</style>
