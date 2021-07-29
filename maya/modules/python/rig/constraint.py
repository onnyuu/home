# coding: utf-8

import maya.cmds as cmds


def apply_constrain():
    selections = cmds.ls(selection=True)
    source_root = selections[0]
    destination_root = selections[1]

    # コンストレインのソースノードをリストアップ
    source_nodes = cmds.listRelatives(source_root, allDescendents=True, type='joint')
    source_nodes.append(source_root)

    locator_shapes = cmds.listRelatives(source_root, allDescendents=True, type='locator')
    if locator_shapes is not None:
        for shape in locator_shapes:
            source_nodes += cmds.listRelatives(shape, parent=True)

    # コンストレインのターゲットノードをリストアップ
    destination_nodes = cmds.listRelatives(destination_root, allDescendents=True, type='joint')
    destination_nodes.append(destination_root)

    locator_shapes = cmds.listRelatives(destination_root, allDescendents=True, type='locator')
    if locator_shapes is not None:
        for shape in locator_shapes:
            destination_nodes += cmds.listRelatives(shape, parent=True)

    # コンストレイン実行
    for source_node in source_nodes:
        for destination_node in destination_nodes:
            if source_node.split("_", 1)[-1]!= destination_node:
                continue

            # point constrain
            if cmds.pointConstraint(destination_node, query=True, name=True) is None:
                    cmds.pointConstraint(source_node, destination_node)

            # orient constrain
            if cmds.orientConstraint(destination_node, query=True, name=True) is None:
                    cmds.orientConstraint(source_node, destination_node)

            # scale constrain
            if cmds.scaleConstraint(destination_node, query=True, name=True) is None:
                    cmds.scaleConstraint(source_node, destination_node)

apply_constrain()