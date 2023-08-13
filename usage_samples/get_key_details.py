import sys

from connectedpapers import ConnectedPapersClient

DEEPFRUITS_PAPER_ID = "9397e7acd062245d37350f5c05faf56e9cfae0d6"


def main() -> int:
    client = ConnectedPapersClient()
    remaining_uses_count = client.sync_get_remaining_usages()
    print(f"Remaining uses count: {remaining_uses_count}")
    free_access_papers = client.sync_get_free_access_papers()
    print(f"Free access papers: {free_access_papers}")
    graph = client.get_graph_sync(DEEPFRUITS_PAPER_ID)
    assert graph.graph_json.start_id == DEEPFRUITS_PAPER_ID
    return 0


if __name__ == "__main__":
    sys.exit(main())