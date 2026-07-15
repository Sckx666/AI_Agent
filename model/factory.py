from abc import ABC, abstractmethod
from langchain_core.embeddings import Embeddings
from langchain_core.language_models import BaseChatModel
from langchain_deepseek import ChatDeepSeek
from langchain_community.embeddings import DashScopeEmbeddings
from utils.config_handler import rag_config


class BaseModelFactory(ABC):
    @abstractmethod
    def generator(self) -> BaseChatModel | Embeddings:
        pass


class ChatModelFactory(BaseModelFactory):
    def generator(self) -> BaseChatModel | Embeddings:
        return ChatDeepSeek(model=rag_config["chat_model_name"],
                            extra_body={"thinking": {"type": rag_config["chat_thinking"]}})


class EmbeddingFactory(BaseModelFactory):
    def generator(self) -> BaseChatModel | Embeddings:
        return DashScopeEmbeddings(model=rag_config["embedding_model_name"])


chat_model = ChatModelFactory().generator()
embedding_model = EmbeddingFactory().generator()
