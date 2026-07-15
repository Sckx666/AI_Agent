from langchain.agents import create_agent

from model.factory import chat_model
from utils.prompt_loader import load_system_prompts
from agent.tools.agent_tools import *
from agent.tools.middlerware import *


class ReactAgent:
    def __init__(self):
        self.agent = create_agent(
            model=chat_model,
            system_prompt=load_system_prompts(),
            tools=[
                rag_summarize,
                get_weather,
                get_user_id,
                get_user_location,
                generate_external_data,
                get_current_month,
                fetch_external_data,
                fill_context_for_report
            ],
            middleware=[
                monitor_tool,
                log_before_model,
                report_prompt_switch,
            ],
        )

    def execute_stream(self, query: str):
        input_dic = {
            "messages": [
                {"role": "user", "content": query},
            ]
        }

        stream = self.agent.stream(input_dic, stream_mode="values", context={"report": False})
        for chunk in stream:
            latest_message = chunk["messages"][-1]
            yield latest_message.content.strip()+'\n'


if __name__ == '__main__':
    react_agent = ReactAgent()
    for _ in react_agent.execute_stream(f"扫地机器人在我所在的地区的气温下如何保养"):
        print(_, end="", flush=True)
