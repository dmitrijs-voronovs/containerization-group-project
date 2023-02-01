<script>
    export let title;
    export let completed;
    export let deleteTodo;
    export let onClick
</script>

<style>
    .completed {
        text-decoration: line-through;
    }
</style>

<div>
    <button on:click={onClick} class:completed={completed}>{title}</button>
    <button on:click={deleteTodo}>Delete</button>
</div>