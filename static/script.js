const todoForm = document.getElementById('form');
const todos = document.getElementById('todos');
const err = document.getElementById('err');
const checkedList = document.querySelectorAll('.check-completed');
const cancelBtns = document.querySelectorAll('.cancel-btn');
const listForm = document.getElementById('listForm');

listForm.addEventListener('submit', async (e) => {
  const textValue = document.querySelector('#listText').value;
  if (!textValue) {
    return;
  }
  e.preventDefault();
  try {
    const response = await fetch('/lists/create', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        new_list: textValue,
      }),
    });
    const addedList = await response.json();
    console.log(addedList);
    const li = document.createElement('li');
    const input = document.createElement('input');
    input.setAttribute('type', 'checkbox');
    li.append(input);
    li.append(addedList.name);
    document.querySelector('#listUl').append(li);
    input.setAttribute('value', '');
  } catch (error) {
    console.log(error);
  }
});

for (let i = 0; i < cancelBtns.length; i++) {
  const btn = cancelBtns[i];
  btn.addEventListener('click', async (e) => {
    try {
      const todoId = e.target.dataset.id;
      response = await fetch(`/todos/${todoId}/delete-todo`, {
        method: 'DELETE',
      });
    } catch (error) {
      console.log(error);
    }
  });
}

for (let i = 0; i < checkedList.length; i++) {
  const item = checkedList[i];
  item.addEventListener('change', async (e) => {
    try {
      const newCompleted = e.target.checked;
      const todoId = e.target.dataset.id;
      const response = await fetch(`/todos/${todoId}/set-completed`, {
        method: 'POST',
        body: JSON.stringify({
          completed: newCompleted,
        }),
        headers: {
          'Content-Type': 'application/json',
        },
      });
    } catch (error) {
      console.log(error);
    }
  });
}

todoForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  const todoText = document.getElementById('todo').value;
  if (!todoText) {
    return;
  }
  try {
    const response = await fetch('/todos/create', {
      method: 'POST',
      body: JSON.stringify({
        description: todoText,
      }),
      headers: {
        'Content-Type': 'application/json',
      },
    });
    const todo = await response.json();
    const listItem = document.createElement('Li');
    const input = document.createElement('input');
    input.setAttribute('type', 'checkbox');
    listItem.append(input);
    listItem.append(todo.description);
    todos.append(listItem);
    err.className = 'hidden';
    e.target.reset();
  } catch (error) {
    console.log(error);
    err.className = '';
  }
});

function createNewTodoLI() {
  const div1 = document.createElement('div');
  const div2 = document.createElement('div');
}
