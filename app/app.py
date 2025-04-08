import json
import asyncio
import pandas as pd

from app.agent import app
from app.config import logger


logger.info("Starting the campaign...")
state_input = json.load(open("events/start.json"))


def get_sample_dataset(sample_size=2):
    df = pd.read_csv("datasets/customers.csv")
    df["age_range"] = pd.qcut(df["Age"], q=3, labels=["low", "medium", "high"])
    df["attr_proportion"] = df.notnull().sum(axis=1) / df.shape[1]
    df["filled"] = pd.cut(df["attr_proportion"], bins=[0, 0.5, 0.9, 1.01], labels=["low", "medium", "high"], include_lowest=True)

    samples = df.groupby(["age_range", "filled"]).apply(
        lambda x: x.sample(n=min(sample_size, len(x)), random_state=42)
    ).reset_index(drop=True)
    samples = samples.drop(columns=["age_range", "filled"])
    return samples.to_dict(orient="records")


async def handler():
    customers = get_sample_dataset()
    for i, client in enumerate(customers):
        logger.info(f"Client: {client}")
        state_input["campaign"]["client"] = client

        result = app.invoke(state_input)

        json.dump(result, open(f"results/email/sample{i}_{client['Age']}.json", "w", encoding="utf8"), indent=4, ensure_ascii=False)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(handler())
    loop.close()