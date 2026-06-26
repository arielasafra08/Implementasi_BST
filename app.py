import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="BST Interactive App",
    page_icon="🌳",
    layout="wide"
)

# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.block-container {
    padding-top: 1rem;
}

.title {
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color:#1e3a8a;
}

.subtitle{
    text-align:center;
    color:gray;
    margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# BST NODE
# =====================================================

class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# =====================================================
# INSERT
# =====================================================

def insert(root, key):

    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)

    elif key > root.key:
        root.right = insert(root.right, key)

    return root

# =====================================================
# SEARCH
# =====================================================

def search(root, key):

    if root is None:
        return False

    if root.key == key:
        return True

    if key < root.key:
        return search(root.left, key)

    return search(root.right, key)

# =====================================================
# DELETE
# =====================================================

def min_value(node):

    current = node

    while current.left:
        current = current.left

    return current

def delete(root, key):

    if root is None:
        return root

    if key < root.key:

        root.left = delete(root.left, key)

    elif key > root.key:

        root.right = delete(root.right, key)

    else:

        if root.left is None:
            return root.right

        elif root.right is None:
            return root.left

        temp = min_value(root.right)

        root.key = temp.key

        root.right = delete(
            root.right,
            temp.key
        )

    return root

# =====================================================
# TRAVERSAL
# =====================================================

def preorder(root, result):

    if root:
        result.append(root.key)
        preorder(root.left, result)
        preorder(root.right, result)

def inorder(root, result):

    if root:
        inorder(root.left, result)
        result.append(root.key)
        inorder(root.right, result)

def postorder(root, result):

    if root:
        postorder(root.left, result)
        postorder(root.right, result)
        result.append(root.key)

# =====================================================
# JUMLAH NODE
# =====================================================

def count_nodes(root):

    if root is None:
        return 0

    return (
        1 +
        count_nodes(root.left) +
        count_nodes(root.right)
    )

# =====================================================
# LEAF NODE
# =====================================================

def count_leaf(root):

    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    return (
        count_leaf(root.left) +
        count_leaf(root.right)
    )

# =====================================================
# HEIGHT BST
# =====================================================

def height(root):

    if root is None:
        return 0

    return 1 + max(
        height(root.left),
        height(root.right)
    )

# =====================================================
# GRAPHVIZ
# =====================================================

def create_graph(root):

    dot = graphviz.Digraph()

    def add(node):

        if node:

            dot.node(
                str(node.key),
                str(node.key)
            )

            if node.left:

                dot.edge(
                    str(node.key),
                    str(node.left.key)
                )

                add(node.left)

            if node.right:

                dot.edge(
                    str(node.key),
                    str(node.right.key)
                )

                add(node.right)

    add(root)

    return dot

# =====================================================
# DATA STUDI KASUS
# =====================================================

data_bst = {

    "🎓 Sistem Data Mahasiswa":
    [2023010,2023005,2023015,
     2023003,2023008,2023012,2023018],

    "🤝 Keanggotaan Koperasi":
    [1001,1005,1003,
     1010,1008,1015],

    "📦 Inventori Toko":
    [501,503,499,
     520,510,530],

    "🏥 Sistem Rekam Medis":
    [2001,2005,1999,
     2010,2003],

    "🏘 Data Penduduk Desa":
    [317401,317402,
     317399,317410,317405],

    "💰 Data Peminjam KDKMP":
    [7001,7005,6999,
     7010,7003,7008]
}

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("🌳 BST MENU")

menu = st.sidebar.selectbox(
    "Pilih Studi Kasus",
    ["🏠 Dashboard"] + list(data_bst.keys())
)

# =====================================================
# DASHBOARD
# =====================================================

if menu == "🏠 Dashboard":

    st.markdown(
        "<div class='title'>🌳 Binary Search Tree Interactive App</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='subtitle'>Modul 9 - Binary Search Tree (BST)</div>",
        unsafe_allow_html=True
    )

    st.info("""
BST (Binary Search Tree) adalah struktur data tree
yang memiliki aturan:

• Node kiri lebih kecil dari root
• Node kanan lebih besar dari root
• Mempercepat proses pencarian data
• Digunakan pada database, indexing, dan searching
""")

    c1,c2,c3 = st.columns(3)

    c1.metric("Jumlah Studi Kasus", "6")
    c2.metric("Operasi BST", "Search/Delete")
    c3.metric("Visualisasi", "Graphviz")

    st.success(
        "Pilih studi kasus pada sidebar untuk melihat implementasi BST."
    )

else:

    root = None

    for item in data_bst[menu]:
        root = insert(root, item)

    st.markdown(
        "<div class='title'>🌳 Binary Search Tree</div>",
        unsafe_allow_html=True
    )

    st.subheader(menu)

    col1,col2,col3 = st.columns(3)

    with col1:
        st.metric(
            "Jumlah Node",
            count_nodes(root)
        )

    with col2:
        st.metric(
            "Leaf Node",
            count_leaf(root)
        )

    with col3:
        st.metric(
            "Tinggi BST",
            height(root)
        )

    st.markdown("---")

    st.header("📋 Data Awal")

    st.write(data_bst[menu])

    st.markdown("---")

    st.header("🔍 Search Node")

    cari = st.number_input(
        "Masukkan data yang dicari",
        step=1
    )

    if st.button("Cari Data"):

        if search(root, cari):
            st.success(
                f"✅ Data {cari} ditemukan dalam BST"
            )

        else:
            st.error(
                f"❌ Data {cari} tidak ditemukan"
            )

    st.markdown("---")

    st.header("🗑 Delete Node")

    hapus = st.number_input(
        "Masukkan data yang ingin dihapus",
        step=1,
        key="hapus"
    )

    if st.button("Hapus Node"):

        root = delete(root, hapus)

        st.success(
            f"Node {hapus} berhasil dihapus"
        )

    st.markdown("---")

    pre = []
    ino = []
    post = []

    preorder(root, pre)
    inorder(root, ino)
    postorder(root, post)

    st.header("📊 Traversal BST")

    tab1,tab2,tab3 = st.tabs(
        ["Preorder","Inorder","Postorder"]
    )

    with tab1:
        st.info(
            " ➜ ".join(map(str, pre))
        )

    with tab2:
        st.success(
            " ➜ ".join(map(str, ino))
        )

    with tab3:
        st.warning(
            " ➜ ".join(map(str, post))
        )

    with st.expander("📖 Penjelasan Traversal"):

        st.write("""
Preorder :
Root → Left → Right

Inorder :
Left → Root → Right

Postorder :
Left → Right → Root

Khusus BST, traversal Inorder akan menghasilkan
data yang sudah terurut secara ascending.
""")

    st.markdown("---")

    st.header("🌳 Visualisasi BST")

    st.graphviz_chart(
        create_graph(root)
    )

    st.markdown("---")

    st.caption(
        "Praktikum Struktur Data - Modul 9 Binary Search Tree"
    )
