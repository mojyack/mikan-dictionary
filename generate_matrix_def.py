# this script is from mecab-as-kkc project.
# https://github.com/ikegami-yukino/mecab-as-kkc

CONNECTION_PATH = "mozc/src/data/dictionary_oss/connection_single_column.txt"
MATRIX_DEF_PATH = "source/system/matrix.def"


def to_matrix(connections):
    num_classes = int(connections[0])
    connection_matrix = ["%s %s" % (num_classes, num_classes)]
    for lid in range(num_classes):
        for rid in range(num_classes):
            line = "%s %s %s" % (lid, rid, connections[lid * num_classes + rid + 1])
            connection_matrix.append(line)
    return "\n".join(connection_matrix)


def main():
    connections = open(CONNECTION_PATH).read()
    connections = connections.splitlines()
    connection_matrix = to_matrix(connections)
    with open(MATRIX_DEF_PATH, "w") as f:
        f.write(connection_matrix)


if __name__ == "__main__":
    main()
