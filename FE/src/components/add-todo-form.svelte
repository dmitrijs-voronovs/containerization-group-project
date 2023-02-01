<script>
    export let addTodo;
    let title = '';

    const handleSubmit = (event) => {
        event.preventDefault();
        addTodo(title);
        title = '';
    }
</script>

<form on:submit={handleSubmit}>
    <input type="text" bind:value={title} />
    <button type="submit">Add Todo</button>
</form>