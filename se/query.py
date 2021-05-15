from __future__ import annotations

import json

import sys


class Node:
    def evaluate(self, index):
        return set()


class Term(Node):
    def __init__(self, term):
        super().__init__()
        self.term = term

    def evaluate(self, index):
        return set(index[self.term])


class Operation(Node):
    def __init__(self, nodes: list[Node]):
        super().__init__()
        self.nodes = nodes

    def combine(self, result, new_results):
        return set()

    def evaluate(self, index):
        result = self.nodes[0].evaluate(index)
        for node in self.nodes[1:]:
            result = self.combine(result, node.evaluate(index))
        return result


class OpAnd(Operation):
    def __init__(self, nodes):
        super().__init__(nodes)

    def combine(self, result, new_results):
        return result & new_results


class OpOr(Operation):
    def __init__(self, nodes):
        super().__init__(nodes)

    def combine(self, result, new_results):
        return result | new_results


def build_query(query):
    node_type = query[0]
    if node_type == "term":
        # ["term", "abelha"]
        return Term(query[1])
    else:
        # ["and", ["term", "abelha"], ["term", "rainha"]]
        arg_list = []
        for arg in query[1:]:
            arg_node = build_query(arg)
            arg_list.append(arg_node)
        if node_type == "and":
            return OpAnd(arg_list)
        elif node_type == "or":
            return OpOr(arg_list)
        else:
            raise KeyError(f"Operação {node_type} desconhecida.")


def parse_raw_query_token(q, cr_token, final_token):

    result = f'["term", "{q[cr_token+1]}"]'
    cr_token += 1
    while cr_token != final_token:
        
        if q[cr_token]  == "or":
            result_or = f'["term", "{q[cr_token-1]}"]'
            res, cr_token = parse_raw_query_token(q, cr_token, final_token)
            result = f'["or", {result_or}, {res}]'
        elif q[cr_token]  == "and":
            result_and =  f'["term", "{q[cr_token-1]}"]'
            res, cr_token = parse_raw_query_token(q, cr_token, final_token)
            result = f'["and", {result_and}, {res}]'
        else:
            cr_token +=1
    
    return result,cr_token


def parse_raw_query(raw_query: str):
    rq = raw_query.split()
    final_token = len(rq)

    if final_token == 1:
        return f'["term", "{rq[0]}"]'
    else:
        return parse_raw_query_token(rq, 0, final_token)

    return  rq


def parse_json_query(json_query: str):
    q = json.loads(json_query)
    print(q)
    query = build_query(q)
    return query

#test section
if __name__ == "__main__":
    print(parse_json_query(parse_raw_query(sys.argv[0])).evaluate())
