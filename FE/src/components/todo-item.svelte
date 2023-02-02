<script>
	export let title;
	export let completed;
	export let deleteTodo;
	export let onClick;
</script>

<div>
	<button on:click={onClick} class:completed>{title}</button>
	<button on:click={deleteTodo}>Delete</button>
</div>

<style>
	.completed {
		text-decoration: line-through;
	}
</style>
