---
title: "30D2R: Active Directory"
date: 2025-08-31
categories: ['30D2R']
---
30D2R: Active Directory

This post is a part of my [30 Days 2 Root](https://dev.to/sshad0w/30-days-to-root-challenge-introduction-3idp) challenge series.
Essentially, I am trying to learn the basics of a different facet of cybersecurity each month. [Click here](https://dev.to/sshad0w/30-days-to-root-challenge-introduction-3idp) to learn about how the challenge works, or tell me what I should study next!

## 1. Active Directory is a map

> Each organization is a world that needs a map to navigate the lay of the land. With this map, administrators know where the valuable things are.
> 
> The issue is...  
> Once attackers own this map, they don't only know *where* the valuable things are, they can control the borders. 

## 2. A breakdown of its components

- Active Directory services are used in the fortune 500.
    
- It's essentially a giant rulebook for an organization that says who can do what, and what they can access, and how they can access resources.
    
### Core components:

- **Users:**     
Individual users with specific security roles and privileges.

- **Groups:** 
Groups are collections of users with specific roles and privileges.

- **Computer accounts:**
Computer accounts are a special type of user with "machine accounts". These often run automated scripts that may read or write to resources on a scheduled interval or if specific conditions are met.
    
- **Domain controllers:**  
These are specific nodes that hold a snapshot of what the map should look like, include the users, groups and permissions associated with the environment.

- **Organizational units:**
These are larger groups. These may have blanket rules applied to them as a whole.

- **Group policy objects:**
The rules set for each organizational unit.

> The Active Directory runs on the back of of LDAP (RFC 4511 and 4519) and Kerberos (RFC 4120)
> 
> Once we get into authentication schemes and access control, this will be referenced again.

## Why attackers *still* care about AD

Whoever controls the map controls the routes. Who may walk to which regions, who gets stopped and questioned, and who is allowed to access specific resources

Attackers may redraw the map in their own favor (basically gerrymandering)  
Granting themselves secret roads, or erasing evidence of their own wrongdoing.

- Persistence
Even if defenders rebuild some towns (Resetting passwords, patching, etc.)  
Attackers can still redraw boundaries at their whim.

Compromising AD isn't like capturing a castle, but controlling GPS. All travelers follow the attacker's false reality.

## Common Active Directory attack paths

**Password spraying:**  
Once inside of an AD environment, attackers can spray for passwords on various users, machine accounts, and domain controllers.

**Group Policy:**  
Since active directory allows multiple users to be managed by a single policy, attackers that can control, modify and set group policies can apply rules to users arbitrarily.

**Kerberos ticket abuse:**
(Kerberoasting, Golden ticket, silver ticket attacks).

**Over permissive service accounts:**
This is is very common attack path for attackers. Often times a service account with a simple password or compromised service tied to a machine account with too many permissions may also allow full domain compromise.

**Cross domain trusts:**
This can allow for multiple domains to be compromised all at once, and may bring down large organizations.

## Why clients care

All enterprises rely on AD for identity management. Without it, it will be extremely different to manage users at scale.

Ransomware groups, APTs and threat actors go directly for it post compromise.

Once the map is taken, there is no defense. All paths can be compromised.

## The wrap

This is an overly simplistic explanation for future posts. This blog merely explains "what AD is" and breadth of common attacks. Even viewing Active directory as the map gives you the edge many attackers nor defenders ever understand.

Never forget: 

Always ask better questions.
