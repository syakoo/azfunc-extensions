# azfunc-extensions
Azure Functions を用いた Python の開発体験(DX)を向上させるために作成した個人ライブラリ

## Document ↔ Dataclass のコンバータ
Azure Function と Cosmos DB は非常に相性がいいですが、Cosmos DB から持ってきたデータは `Document` クラスのインスタンスです。
コイツが使いにくくデータベースのパラメータが何だったのか、型は何だったのかがよくわからなくなります。

ということで、予め自分で作成した `dataclass` へ変換する関数を作成しました。それが `doc2dc()` です

### doc2dc()

```python
from dataclasses import dataclass

from azfunc_extensions import doc2dc


@dataclass
class User:
    name: str
    age: int

# Document → User
user = doc2dc(doc, User)
print(user.name, user.id)
```

そして、保存するときも `Document` に直す必要があるため、`dataclass` から `Document` へ変換する `dc2doc()` も作成しました:

### dc2doc()
```python
from dataclasses import dataclass

from azfunc_extensions import dc2doc


@dataclass
class User:
    name: str
    age: int

user = User("syakoo", 22)
# User → Document
doc = dc2doc(user) # <azure.Document at 0x7f189f516160>
```
