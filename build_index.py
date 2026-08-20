from rag.vector_store import BugVectorStore

store = BugVectorStore()
store.build("bug_dataset.csv")

print("✅ Index Ready")