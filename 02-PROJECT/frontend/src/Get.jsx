import { createResource, Show, For } from "solid-js";

export default function Get() {
  const fetchClients = async () => {
    const res = await fetch("http://127.0.0.1:8000/clients");
    if (!res.ok) throw new Error("Network error");
    return res.json();
  };

  const [clients, { refetch }] = createResource(fetchClients);

  return (
    <>
      <Show when={!clients.loading} fallback={<p>Loading...</p>}>
        <div>
          <For each={clients()}>
            {(client) => (
              <div>
                <h3>{client.name}</h3>
                <p>{client.text}</p>
              </div>
            )}
          </For>
        </div>
      </Show>
    </>
  );
}
