paramater = {
    "lambda": {
        "hello": {
            "env": {
                "LOG_LEVEL": "INFO",
            },
            "memory_size": 128,
        },
    },
}


def build_name(service: str, hostname: str) -> str:
    return f"integ-{service}-{hostname}"
