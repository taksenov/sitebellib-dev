# coding=utf-8


def create_profile(sender, instance, signal, created, **kwargs):
    """When user is created also create a matching profile."""

    from elcatuserprofile.models import chb

    if created:
        chb(user = instance).save()
        # Do additional stuff here if needed, e.g.
        # create other required related records