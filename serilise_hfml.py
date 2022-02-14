import yaml
from pathlib import Path
from openpecha.serializers import HFMLSerializer

def from_yaml(yml_path):
    return yaml.safe_load(yml_path.read_text(encoding="utf-8"))

def get_hfml_text(opf_path, index=None):
    """Return hmfl of text from the pecha opf

    Args:
        opf_path (str): opf path
        text_id (str): text id
        index (dict, optional): pecha index. Defaults to None.

    Returns:
        dict: vol id as key and hfml as the content
    """
    serializer = HFMLSerializer(
        opf_path, index_layer=index, layers=["Pagination"]
    )
    serializer.apply_layers()
    hfml_text = serializer.get_result()
    return hfml_text


def save_hfml(hfml, parma):
    if hfml:
        for vol_id, hfml_text in hfml.items():
            Path(f'./hfmls/{parma}/{vol_id}.txt').write_text(hfml_text, encoding='utf-8')
        print('')

if __name__ == "__main__":
    parma = "derge_parphud"
    opf_path = Path('./opfs/e7a2a7b36dc54d56af46981d0d728beb/e7a2a7b36dc54d56af46981d0d728beb.opf')
    
    # parma = "esu_derge"
    # opf_path = Path('./opfs/P000001/P000001.opf')
    index = from_yaml((opf_path / "index.yml"))
    hfmls = get_hfml_text(opf_path,index=index)
    save_hfml(hfmls, parma)