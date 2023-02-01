<script>
    import TodoList from './components/todo-list.svelte';
    import AddTodoForm from './components/add-todo-form.svelte';

    let todos = [
        {id: 1, title: 'Todo 1', completed: false},
        {id: 2, title: 'Todo 2', completed: true},
        {id: 3, title: 'Todo 3', completed: false},
    ];

    const addTodo = (title) => {
        todos = [...todos, { id: todos.length + 1, title, completed: false }];
    };

    const deleteTodo = (id) => {
        todos = todos.filter(todo => todo.id !== id);
    };

    const toggleCompleted = (id) => {
        todos = todos.map(todo => {
            if (todo.id === id) {
                return { ...todo, completed: !todo.completed };
            }
            return todo;
        });
    };
</script>

<style>
	main {
		text-align: center;
	}
</style>

<main>
<h1>TODO App</h1>
<TodoList todos={todos} deleteTodo={deleteTodo} toggleCompleted={toggleCompleted} />
<AddTodoForm addTodo={addTodo} />
</main>