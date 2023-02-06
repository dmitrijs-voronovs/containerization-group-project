<script>
	import TodoList from "./components/todo-list.svelte";
	import AddTodoForm from "./components/add-todo-form.svelte";
	import { onMount } from "svelte";

	const BE_URL = "api";
	function getCookie(name) {
		const match = document.cookie.match(
			new RegExp("(^| )" + name + "=([^;]+)")
		);
		if (match) return match[2];
	}
	const csrftoken = getCookie("csrftoken");
	const headers = new Headers();
	headers.append("X-CSRFToken", csrftoken);
	const fetchWithCSRF = (url, opts) =>
		// fetch(url, { ...opts, headers, credentials: "include" });
		fetch(url, { ...opts, headers });

	let todos = [];

	onMount(async function () {
		const response = await fetchWithCSRF(`${BE_URL}/todos/`);
		const data = await response.json();
		todos = data.results;
	});

	async function createTodo(title) {
		const response = await fetchWithCSRF(`${BE_URL}/todos/create/`, {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify({ title: title }),
		});
		const data = await response.json();
		todos = [...todos, data];
	}

	async function updateTodo(item) {
		const { id } = item;
		const response = await fetchWithCSRF(`${BE_URL}/todos/${id}/update/`, {
			method: "PUT",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify(item),
		});
		const data = await response.json();
		todos = todos.map((todo) => (todo.id === id ? data : todo));
	}

	async function deleteTodo(id) {
		await fetchWithCSRF(`${BE_URL}/todos/${id}/delete/`, {
			method: "DELETE",
		});
		todos = todos.filter((todo) => todo.id !== id);
	}

	async function toggleTodo(id) {
		const todo = todos.find((todo) => todo.id === id);
		await updateTodo({ ...todo, completed: !todo.completed });
	}
</script>

<main>
	<h1>TODO App</h1>
	<TodoList {todos} {deleteTodo} {toggleTodo} />
	<AddTodoForm addTodo={createTodo} />
</main>

<style>
	main {
		text-align: center;
	}
</style>
