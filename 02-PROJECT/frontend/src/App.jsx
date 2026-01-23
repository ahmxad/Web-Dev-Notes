import { createResource, Show, For } from "solid-js";

export default function App() {
  const fetchBooks = async () => {
    const res = await fetch("http://127.0.0.1:8000/books");
    if (!res.ok) throw new Error("Network error");
    return res.json();
  };

  const [books] = createResource(fetchBooks);

  return (
    <>
      <Show when={!books.loading} fallback={<p>Loading...</p>}>
        <div>
          <For each={books()}>
            {(book) => (
              <div>
                <h3>{book.name}</h3>
                <p>{book.year}</p>
              </div>
            )}
          </For>
        </div>
      </Show>
    </>
  );
}
