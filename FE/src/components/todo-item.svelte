<script>
	export let title;
	export let completed;
	export let deleteTodo;
	export let toggleTodo;
</script>

<div>
	<button on:click={toggleTodo} class:completed>{title}</button>
	<button on:click={deleteTodo}>Delete</button>
</div>

<style>
	.completed {
		text-decoration: line-through;
	}
</style>
