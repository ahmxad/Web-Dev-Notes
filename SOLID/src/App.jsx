import { createResource } from "solid-js";

export default function App() {
  const fetchPosts = async () => {
    const res = await fetch("https://jsonplaceholder.typicode.com/posts");
    if (!res.ok) throw new Error("Network error");
    return res.json();
  };

  const [posts] = createResource(fetchPosts);

  return (
    <>
      <Show when={!posts.loading} fallback={<p>Loading...</p>}>
        <div>
          <For each={posts()}>
            {(post) => (
              <div>
                <h3>{post.title}</h3>
                <p>{post.body}</p>
              </div>
            )}
          </For>
        </div>
      </Show>
    </>
  );
}
