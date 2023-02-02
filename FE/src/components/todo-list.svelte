<script>
	import TodoItem from "./todo-item.svelte";

	export let todos;
	export let deleteTodo;
	export let toggleTodo;
</script>

<ul>
	{#each todos as todo}
		<TodoItem
			title={todo.title}
			completed={todo.completed}
			deleteTodo={() => deleteTodo(todo.id)}
			onClick={() => toggleTodo(todo.id)}
		/>
	{/each}
</ul>

<style>
	ul {
		list-style: none;
		padding: 0;
	}
</style>
