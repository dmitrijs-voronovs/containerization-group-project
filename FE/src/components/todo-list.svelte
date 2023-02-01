<script>
    import TodoItem from './todo-item.svelte';

    export let todos;
    export let deleteTodo;
    export let toggleCompleted;
</script>

<ul>
    {#each todos as todo}
        <TodoItem 
            title={todo.title} 
            completed={todo.completed}
            deleteTodo={() => deleteTodo(todo.id)}
            onClick={() => toggleCompleted(todo.id)}
        />
    {/each}
</ul>