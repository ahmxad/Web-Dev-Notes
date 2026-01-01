import { createResource, Show, For } from "solid-js";
import axios from "axios";

export default function App() {
  const fetchUsers = async () => {
    const res = await axios.get("http://127.0.0.1:8000/users");
    return res.data;
  };
  
  const [users, { refetch }] = createResource(fetchUsers);

  const deleteAllUsers = async () => {
    await axios.delete("http://127.0.0.1:8000/users");
    refetch(); // 👈 UI refresh without page reload
  };
  const deleteUser = async (id) => {
  await axios.delete(`http://127.0.0.1:8000/users/${id}`);
  refetch(); // UI sync
};
  return (
    <>
    <Show when={!users.loading} fallback={<p>Loading...</p>}>
      <For each={users() || []}>{(user) => <p>id: {user.id} --- email: ({user.email})
        <button onClick={() => deleteUser(user.id)}>
        Delete
      </button>
        </p>}</For>
    </Show>
    <button onClick={deleteAllUsers}>
        Delete All Users
      </button>
    </>
  );
}
