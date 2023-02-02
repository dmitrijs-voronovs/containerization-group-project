<script>
	export let addTodo;
	let title = "";

	const handleSubmit = (event) => {
		event.preventDefault();
		addTodo(title);
		title = "";
	};
</script>

<form on:submit={handleSubmit}>
	<input type="text" bind:value={title} />
	<button type="submit">Add Todo</button>
</form>

<style>
	form {
		display: flex;
		margin-top: 1rem;
	}

	input[type="text"] {
		flex-grow: 1;
		padding: 0.5rem;
		margin-right: 1rem;
	}

	button[type="submit"] {
		padding: 0.5rem 1rem;
		background-color: rgb(94, 194, 228);
		color: white;
		border: none;
		border-radius: 4px;
		cursor: pointer;
	}

	button[type="submit"]:hover {
		background-color: blue;
	}
</style>
