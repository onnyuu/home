# coding: utf-8
"""
IKとFKのRig階層を出力階層とコンストレインする
"""


import maya.cmds as cmds


def apply_constrain(kinematics='Ik'):
    """
    :param kinematics: IKかIKか
    :type kinematics: str
    :return:
    """
    reverse_dict = {'Ik': 'Fk', 'Fk': 'Ik'}
    sel = cmds.ls('{}_ds_Hips'.format(kinematics))[0]
    nodes = cmds.listRelatives(sel, allDescendents=True, type='joint')
    nodes.append(sel)
    locator_shapes = cmds.listRelatives(sel, allDescendents=True, type='locator')

    for shape in locator_shapes:
        nodes += cmds.listRelatives(shape, parent=True)

    for node in nodes:
        name = node.split('{}_ds_'.format(kinematics))[-1]
        target_node = 'ME:{}'.format(name)
        rev_node = '{}_ds_{}'.format(reverse_dict[kinematics], name)

        if cmds.parentConstraint(node, query=True, name=True) is not None:
            if cmds.parentConstraint(target_node, query=True, name=True) is None:
                if kinematics == 'Ik':
                    cmds.parentConstraint(node, target_node)
                    cmds.parentConstraint(rev_node, target_node)
                else:
                    cmds.parentConstraint(rev_node, target_node)
                    cmds.parentConstraint(node, target_node)

        if cmds.pointConstraint(node, query=True, name=True) is not None:
            if cmds.pointConstraint(target_node, query=True, name=True) is None:
                if kinematics == 'Ik':
                    cmds.pointConstraint(node, target_node)
                    cmds.pointConstraint(rev_node, target_node)
                else:
                    cmds.pointConstraint(rev_node, target_node)
                    cmds.pointConstraint(node, target_node)

        if cmds.orientConstraint(node, query=True, name=True) is not None:
            if cmds.orientConstraint(target_node, query=True, name=True) is None:
                if kinematics == 'Ik':
                    cmds.orientConstraint(node, target_node)
                    cmds.orientConstraint(rev_node, target_node)
                else:
                    cmds.orientConstraint(rev_node, target_node)
                    cmds.orientConstraint(node, target_node)

        if cmds.scaleConstraint(node, query=True, name=True) is not None:
            if cmds.scaleConstraint(target_node, query=True, name=True) is None:
                if kinematics == 'Ik':
                    cmds.scaleConstraint(node, target_node)
                    cmds.scaleConstraint(rev_node, target_node)
                else:
                    cmds.scaleConstraint(rev_node, target_node)
                    cmds.scaleConstraint(node, target_node)

    print('Finish - apply constraint for {}'.format(kinematics))


apply_constrain(kinematics='Ik')
apply_constrain(kinematics='Fk')