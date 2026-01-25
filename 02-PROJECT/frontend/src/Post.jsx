import { createSignal } from "solid-js";

export default function Post() {
  const [name, setName] = createSignal("");
  const [text, setText] = createSignal("");
  const [loading, setLoading] = createSignal(false);
  const [error, setError] = createSignal("");

  const submitForm = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");

    try {
      const res = await fetch("http://127.0.0.1:8000/clients", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: name(),
          text: text(),
        }),
      });

      if (!res.ok) {
        throw new Error("Failed to send data");
      }

      // optional: response ka data
      await res.json();

      // form reset
      setName("");
      setText("");
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };
  
  return (
    <form onSubmit={submitForm}>
      <input
        type="text"
        placeholder="Client name"
        value={name()}
        onInput={(e) => setName(e.target.value)}
      />

      <textarea
        placeholder="Client note"
        value={text()}
        onInput={(e) => setText(e.target.value)}
      />

      <button type="submit" disabled={loading()}>
        {loading() ? "Sending..." : "Send"}
      </button>

      {error() && <p style={{ color: "red" }}>{error()}</p>}
    </form>
  );
}
