---
layout: post
title: How to Update Arch Linux Mirrorlist by Country
description: This article provides instructions on how to update the Arch Linux mirrorlist by country. The mirrorlist is a list of servers that Arch Linux uses to download packages. By updating the mirrorlist, you can ensure that you are using the most up-to-date and reliable mirrors for your country.
keywords: ArchLinux, mirrorlist, reflector
tags: linux archlinux 
---
This article provides instructions on how to update the Arch Linux mirrorlist by country. The mirrorlist is a list of servers that Arch Linux uses to download packages. By updating the mirrorlist, you can ensure that you are using the most up-to-date and reliable mirrors for your country.

## Install reflector

    sudo pacman -S reflector

## Generate a new mirrorlist for your country

    reflector --country <country code> --latest 5 --sort rate --save /etc/pacman.d/mirrorlist

Replace `<country code>` with the two-letter country code for the
country you want to refresh. For example, to refresh the mirrorlist for
the United States, you would run the following command:

    reflector --country US --latest 5 --sort rate --save /etc/pacman.d/mirrorlist

Once the new mirrorlist has been generated, you can force pacman to
refresh the package lists by running the following command:

    pacman -Syyu --refresh

This will ensure that you are using the latest mirrors for your country.

## Here are some additional tips for refreshing your mirrorlist:

You can use the `--country` flag to specify multiple countries. For
example, to refresh the mirrorlist for the United States and Canada, you
would run the following command:

    reflector --country US,CA --latest 5 --sort rate --save /etc/pacman.d/mirrorlist

You can use the `--latest` flag to specify the number of mirrors you
want to keep. The default is 5. You can use the `--sort` flag to specify
how you want the mirrors to be sorted. The default is by rate. You can
also sort by latency or last update. You can use the `--save` flag to
specify the file where you want the new mirrorlist to be saved. The
default is /etc/pacman.d/mirrorlist.
